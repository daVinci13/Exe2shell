use std::env;
use std::fs::File;
use std::io::Read;

fn read_file(file_location: &str) -> Option<Vec<u8>> {
    let mut file = File::open(file_location).ok()?;
    let mut buffer = Vec::new();
    file.read_to_end(&mut buffer).ok()?;
    Some(buffer)
}

fn format_content(content: Option<Vec<u8>>) -> Option<String> {
    content.map(|bytes| bytes.iter().map(|b| format!("\\x{:02x}", b)).collect())
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
        eprintln!("Please provide a file name as an argument.");
        return;
    }
    let file_location = &args[1];
    let content = read_file(file_location);
    let formatted_content = format_content(content);
    if let Some(formatted_content) = formatted_content {
        println!("{}", formatted_content);
    }
}
