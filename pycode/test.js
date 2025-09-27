function outer(func) {
  function inner(name) {
    console.log('inner')
    func(name)
  }
  return inner
}

function test(name) {
  console.log('test', name)
}
test = outer(test)
test('zhangsan')
