import retro
import numpy as np
import cv2
import neat
import pickle
import os

env = retro.make('DonkeyKongCountry-Snes', '1Player.CongoJungle.RopeyRampage.Level2')

imgarray = []

def main(genomes, config):
    
    for genome_id, genome in genomes:
        ob = env.reset()
        ac = env.action_space.sample()

        inx, iny, inc = env.observation_space.shape

        inx = int(inx/8)
        iny = int(iny/8)

        net = neat.nn.recurrent.RecurrentNetwork.create(genome, config)

        current_max_fitness = 0
        fitness_current = 0
        frame = 0
        counter = 0
        xpos = 0
        xpos_max = 0

        done = False

        while not done:
            env.render()
            frame += 1

            ob = cv2.resize(ob, (inx, iny))
            ob = cv2.cvtColor(ob, cv2.COLOR_BGR2GRAY)
            ob = np.reshape(ob, (inx, iny))

            for x in ob:
                for y in x:
                    imgarray.append(y)

            nnOutput = net.activate(imgarray)

            ob, rew, done, info = env.step(nnOutput)
            
            #print(env.get_action_meaning(nnOutput))
            #print(info)
            imgarray.clear()
            
            xpos = info['x']
            #print(xpos)

            if xpos > xpos_max:
                fitness_current += 1
                xpos_max = xpos

            if fitness_current > current_max_fitness:
                current_max_fitness = fitness_current
                counter = 0
            else:
                counter += 1

            if done or counter == 250:
                done = True
                print(genome_id, fitness_current)

            genome.fitness = fitness_current


config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, os.path.join(os.path.dirname(__file__), "config_feedforward.txt"))

p = neat.Population(config) 

winner = p.run(main)

env.reset()

done = False

while not done:
    env.render()
    action = env.action_space.sample()
    print(action)
    #print(env.get_action_meaning(action))
    ob, rew, done, info = env.step(action)
