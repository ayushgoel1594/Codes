class test{
   public static void main(String[] args) {
        System.out.println("ayush is great");
        B b = new B();
    }
}

class A{
    int a;
    A(){
        System.out.println("A");
    }
    A(int c){
        System.out.println(c);
    }
}
class B extends A{
    int b;
    B(){
        super(5);
        System.out.println("B");
    }
}