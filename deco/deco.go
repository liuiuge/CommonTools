package deco

import (
	"errors"
	"fmt"
)

func retry2() error {
	fmt.Println("st", s_t)
	if s_t < 1 {
		s_t++
		return errors.New("too small")
	}
	return nil
}

func decRetry3(r_t int, f func() error) func() error {
	return func() error {
		fmt.Println("start")
		fmt.Println("r_t", r_t)
		var err error
		for i := 0; i < r_t; i++ {
			err = f()
			if err == nil {
				fmt.Println("rt", i)
				s_t = 0
				return nil
			}
		}
		fmt.Println("end")
		return err
	}
}

func main() {
	// test1()
	//test3()
	//fmt.Println(decorator(Hello)("hello world"))
	//fmt.Println(decRetry2(2))
	fmt.Println(decRetry3(2, retry2)())
}
