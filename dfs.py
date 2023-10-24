class environment(object):
    #defining the possible paths from a vertex
    mygraph = {
            "1":set(["2","3"]),
            "2":set(["1","4"]),
            "3":set(["1","4"]),
            "4":set(["2","3"])
        }

    state = "2"
    goal = "4"

#a class to implement dfs
class agent (environment):
    #this function looks through all available paths and returns
    def dfs(graph,start,goal):
        stack = [(start,[start])]
        p = []
        while stack:
            (vertex,path) = stack.pop()
            print('path is - ',path)
            for next in graph[vertex]-set(path):
                print('next is - ', next)
                if next == goal:
                    p.append(path+[next])
                else:
                    stack.append((next,path+[next]))
        return p

    def __init__(self,environment):
        print("dfs-all paths",
        agent.dfs(environment.mygraph,environment.state,environment.goal))

e1 = environment()
a1 = agent(e1)