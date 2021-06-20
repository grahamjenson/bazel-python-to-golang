package main

import "C"
import "fmt"

//export hello
func hello(inputC *C.char) *C.char {
 	input := C.GoString(inputC)
 	return C.CString(fmt.Sprintf("Hello %s", input))
 }
 
 func main() {}