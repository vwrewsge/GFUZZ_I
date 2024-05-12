
(module
  (func $log (import "env" "consoleLog") (param i32))
  (func (export "add") (param i32 i32) (result i32)
    local.get 0
    local.get 1
    i32.add)
  (export "memory" (memory 1))
  (export "log" (func $log))
)
