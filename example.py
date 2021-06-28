import retro


def main():
    #env = retro.make(game='Airstriker-Genesis')
    env = retro.make(game='RoadFighterLvl')
    #env = retro.make(game='RoadFighter-Nes', state='RoadFighter.Level{}'.format(1))
    obs = env.reset()
    while True:
        obs, rew, done, info = env.step(env.action_space.sample())
        env.render()
        if done:
            obs = env.reset()
    env.close()


if __name__ == "__main__":
    main()
