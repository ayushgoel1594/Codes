class static_and_final {
    public static void main(String[] args) {
        A a = new B();
        // System.out.println(a.a);
         System.out.println(A.st);

        B b = new B();
        //System.out.println(A.st);
    }
}

class A {
    int a = 4;
    //when static members are inherited, they work as one for both the classes
    static int st=1;
    A() {
        st++;
        System.out.println("inside A constructor");
    }

    // if we make the method final, it cannot be overriden
    final void func(){
        System.out.println("inside base func");
    }

}

class B extends A {
    int a = 5;
    int b;

  
    //cannot give sysout directly here, it will be an error
    //System.out.println("Dsad");
    B() {
        st++;
        System.out.println("inside B constructor1");
    }
    

    //static block is executed first, if it is present, even before the constructor
    //sop statements are allowed inside the static block
    static{
        System.out.println("Static block executed");
    }

    //func will give error, if base class method is final
    // void func(){
    //     System.out.println("inside child func");
    // }


}