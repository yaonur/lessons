#[allow(unused_variables)]
#[allow(unused_assignments)]
fn main() {
    let name = "Alex";
    let mut age = 32;
    age = 43;
    let color = "blue";
    let color = 18;

    let (a, b, c) = (42, 82, "red");
    let pi: f32 = 4.0;
    let million = 1_000_000;
    let char1 = '👉';
    let smiley = '🤔';
    let cat: &'static str = "Fluffy";
    println!("cat is {}", cat);
    let dog = String::new();
    let dog = "dog".to_string();
    let mut dog = String::from("maxyDog");
    dog = "daumdus".to_string();
    println!("dog is {}", dog);
    let owner = format!("Hey im the owner of {}", dog);
    println!("owner is {}", owner);
    println!("length of dog:{}",dog.len());
    dog.push_str(" the dog");
    println!("the dog after push {}",dog)
}
