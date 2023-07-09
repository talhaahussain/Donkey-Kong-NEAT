import retro

env = retro.make('DonkeyKongCountry-Snes', '1Player.CongoJungle.RopeyRampage.Level2')

env.reset()

done = False

while not done:
    env.render()
    action = env.action_space.sample()    
    env.step(action)
