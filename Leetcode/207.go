package main

func isCycle(u int, adj [][]int, check []int) bool {
	check[u] = 1
	for _, v := range adj[u] {
		if check[v] == 1 {
			return true
		} else if check[v] == 0 {
			if isCycle(v, adj, check) {
				return true
			}
		}
	}
	check[u] = 2
	return false
}

func canFinish(numCourses int, prerequisites [][]int) bool {
	adj := make([][]int, numCourses)

	for i := 0; i < numCourses; i++ {
		adj[i] = make([]int, 0)
	}
	for _, edge := range prerequisites {
		adj[edge[0]] = append(adj[edge[0]], edge[1])
	}
	check := make([]int, numCourses)
	for u := 0; u < numCourses; u++ {
		if isCycle(u, adj, check) {
			return false
		}
	}
	return true

}
