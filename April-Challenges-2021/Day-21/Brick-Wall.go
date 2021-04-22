func leastBricks(wall [][]int) int {
	ret := 0
	hashTable := map[int]int{}
	
	for i := range wall {
		curWidth := 0
		for j := 0; j < len(wall[i])-1; j++ {
			curWidth += wall[i][j]
			hashTable[curWidth]++
		}
	}
	for _, v := range hashTable {
		if v > ret {
			ret = v
		}
	}
	return len(wall) - ret  
}
