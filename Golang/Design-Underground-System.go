type UndergroundSystem struct {
    Trip map[int][]string;
    Time map[int][]int;
    Trips map[string][]float64;
}


func Constructor() UndergroundSystem {
    
    system := UndergroundSystem{
        Trip: map[int][]string{},
        Time: map[int][]int{},
        Trips: map[string][]float64{},
    }
    
    return system
}


func (this *UndergroundSystem) CheckIn(id int, stationName string, t int)  {
    this.Trip[id] = []string{}
    this.Time[id] = []int{}
    this.Trip[id] = append(this.Trip[id], stationName)
    this.Time[id] = append(this.Time[id], t)
}


func (this *UndergroundSystem) CheckOut(id int, stationName string, t int)  {
    this.Trip[id] = append(this.Trip[id], stationName)
    this.Time[id] = append(this.Time[id], t)
    
    diff := float64(this.Time[id][1] - this.Time[id][0])
    
    firstStation := this.Trip[id][0]
    secondStation := this.Trip[id][1]
    
    direct1 := fmt.Sprintf("%v-%v",firstStation, secondStation)
    
    if this.Trips[direct1] == nil {
        this.Trips[direct1] = append(this.Trips[direct1], diff)
    } else {
        this.Trips[direct1][0]+=diff
    }

    
    if len(this.Trips[direct1]) == 1 {
        this.Trips[direct1] = append(this.Trips[direct1], 1)
    } else {
        this.Trips[direct1][1]+=1
    }

}


func (this *UndergroundSystem) GetAverageTime(startStation string, endStation string) float64 {
    direction1 := fmt.Sprintf("%v-%v", startStation, endStation)
    return this.Trips[direction1][0]/this.Trips[direction1][1]
}


/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * obj := Constructor();
 * obj.CheckIn(id,stationName,t);
 * obj.CheckOut(id,stationName,t);
 * param_3 := obj.GetAverageTime(startStation,endStation);
 */
