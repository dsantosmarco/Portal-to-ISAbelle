from pisa_client import initialise_env


if __name__ == '__main__':
    env = initialise_env(
        8001, 
        "/home/qj213/Isabelle2021", 
        "/home/qj213/afp-2021-10-22/thys/Real_Impl/Real_Impl_Auxiliary.thy", 
        "/home/qj213/afp-2021-10-22/thys/Real_Impl"
    )
    env.proceed_to_line('end', 'before')
    env.initialise()
    env.step_to_top_level_state('lemma primes_infinite: "\<not> (finite {(p::nat). prime p})"', "default", "test")
    print(env.step_to_top_level_state('normalhammer', 'test', 'test1'))
    print(env.step_to_top_level_state('normalhammer primes_infinite', 'test', 'test2'))
    print(env.step_to_top_level_state('normalhammer primes_infinite,bigger_prime', 'test', 'test3'))
