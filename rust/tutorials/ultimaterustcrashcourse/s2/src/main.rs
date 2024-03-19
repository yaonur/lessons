fn main() {
    shadow();
    memory_safety_init_var();
}
fn shadow() {
    let x = 10;
    {
        let x = 20;
        println!("{}", x); // 20
    }
    println!("{}", x); // 10
}

fn memory_safety_init_var(){
    let mut enigma: i32;
    // println!("{}", enigma); // wont work
    if true {
        enigma = 3;
        println!("{}", enigma);
    } else {
        enigma = 7;
    }
    println!("{}", enigma); // error if not else block before build rust saves day 
}
