import mesa
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import matplotlib
matplotlib.use('TkAgg')
ENABLE_RENDERING = True


class RobotAgent(mesa.Agent):
    def __init__(self, model, instructions):
        super().__init__(model)
        self.instructions = instructions
        self.cursor = 0

    def step(self):
        x, y = self.pos
        dx, dy = 0, 0
        if self.cursor < len(self.instructions):
            if self.instructions[self.cursor] == "<":
                dx, dy = -1, 0
            elif self.instructions[self.cursor] == "^":
                dx, dy = 0, -1
            elif self.instructions[self.cursor] == ">":
                dx, dy = 1, 0
            elif self.instructions[self.cursor] == "v":
                dx, dy = 0, 1

            self.cursor += 1

        new_pos = (x + dx, y + dy)

        if not self.model.grid.out_of_bounds(new_pos):
            contents = self.model.grid.get_cell_list_contents([new_pos])
            if any(isinstance(agent, WallAgent) for agent in contents):
                return

            for agent in contents:
                if isinstance(agent, BoxAgent):
                    if not agent.push(dx, dy):
                        return

            self.model.grid.move_agent(self, new_pos)


class BoxAgent(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)

    def push(self, dx, dy):
        x, y = self.pos
        new_pos = (x + dx, y + dy)

        if not self.model.grid.out_of_bounds(new_pos):
            contents = self.model.grid.get_cell_list_contents([new_pos])
            for agent in contents:
                if isinstance(agent, WallAgent):
                    return False
                if isinstance(agent, BoxAgent):
                    if not agent.push(dx, dy):
                        return False

            self.model.grid.move_agent(self, new_pos)
            return True
        return False


class WallAgent(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)


class WarehouseModel(mesa.Model):
    def __init__(self, width, height, seed=None):
        super().__init__(seed=seed)
        self.grid = mesa.space.SingleGrid(width, height, False)

    def init_agents(self, boxes, walls, robot, instructions):
        for pos in boxes:
            box = BoxAgent(self)
            self.grid.place_agent(box, pos)

        for pos in walls:
            wall = WallAgent(self)
            self.grid.place_agent(wall, pos)

        robot_agent = RobotAgent(self, instructions)
        self.grid.place_agent(robot_agent, robot)

    def step(self):
        for agent in self.agents:
            agent.step()

    def get_grid_matrix(self):
        grid_matrix = np.zeros((self.grid.width, self.grid.height))
        for cell_content, (x, y) in self.grid.coord_iter():
            if isinstance(cell_content, BoxAgent):
                grid_matrix[x, y] = 1
            elif isinstance(cell_content, WallAgent):
                grid_matrix[x, y] = 2
            elif isinstance(cell_content, RobotAgent):
                grid_matrix[x, y] = 3
        return grid_matrix.T


def animate(frame):
    model.step()
    if ENABLE_RENDERING:
        grid_matrix = model.get_grid_matrix()
        ax.clear()
        sns.heatmap(
            grid_matrix,
            cmap="viridis",
            annot=False,
            cbar=False,
            square=True,
            xticklabels=False,
            yticklabels=False,
            ax=ax,
        )
        ax.set_title(f"Step {frame + 1}")


if __name__ == "__main__":
    boxes = []
    walls = []
    instructions = []
    grid_size = (0, 0)

    with open("input.txt") as f:
        for i, line in enumerate(f):
            for j, c in enumerate(line):
                if c == "O":
                    boxes.append((j, i))
                elif c == "#":
                    walls.append((j, i))
                    grid_size = (j, i)
                elif c == "@":
                    robot = (j, i)
            if "<" in line or ">" in line or "^" in line or "v" in line:
                instructions.extend(list(line.strip()))

    model = WarehouseModel(grid_size[0] + 1, grid_size[1] + 1)
    model.init_agents(boxes, walls, robot, instructions)

    fig, ax = plt.subplots(figsize=(5, 5))

    anim = FuncAnimation(
        fig, animate, frames=len(instructions), interval=10, repeat=False
    )

    plt.show()

    score = 0
    for agent in model.agents:
        if isinstance(agent, BoxAgent):
            score += agent.pos[1] * 100 + agent.pos[0]

    print('1:', score)
