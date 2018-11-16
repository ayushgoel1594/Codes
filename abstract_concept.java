class abstract_concept {
    public static void main(String[] args) {
        A a = new B();
        // System.out.println(a.a);
        // System.out.println(A.st);

        B b = new B();

        //we cannot initialize A, as it is an abstract class
        // A a = new A();
    }
}

abstract class A {
    int a = 4;
   
    A() {
       
        System.out.println("inside A constructor");
    }

    //derived class must override this method, otherwise it will lead to an error
    abstract void ayush();

    //derived class may or may not override this method
    void raj(){

    }

}

class B extends A {
    int a = 5;
    
    B() {
     
        System.out.println("inside B constructor1");
    }

    //if this is not overridden it will lead to an error
    void ayush(){
        System.out.println("This must be overridden");
    }

   


}