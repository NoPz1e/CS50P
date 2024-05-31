def main():    
  name = input("What's yout name? ").strip().title()
  hello(name)
  
  def hello(to="world"):
    print(f"Hello, {to}")
    
main()