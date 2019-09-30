package deco

import (
	"errors"
	"fmt"
)
var s_t = 0
// 示例函数
func retry2() error {
	fmt.Println("st", s_t)
	if s_t < 1 {
		s_t++
		return errors.New("too small")
	}
	return nil
}
// 装饰器本体
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
// 使用例子
func main() {
	fmt.Println(decRetry3(2, retry2)())
}
