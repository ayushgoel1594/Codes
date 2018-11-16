class overriding {
    public static void main(String[] args) {
        A a = new B();
        System.out.println(a.a);
        a.func();
        int c=4,b=5;
        if(c=b)
        System.out.println("yes");
        else
        System.out.println("no");

    }
}

class A {
    int a = 4;

    A() {
        System.out.println("inside A constructor");
    }

    A(int c) {
        System.out.println("inside a parametrised constructor:"+c);
    }

    public void func() {
        System.out.println("In parent");
    }

    // if this is commented hashcode of the object will be printed on printing the
    // object
    public String toString() {
        return "Ayush64648";
    }

}

class B extends A {
    int a = 5;
    int b;

    
    //cannot give sysout directly here, it will be an error
    //System.out.println("Dsad");
    B() {
        //Base class constructor is called
        super(5);
        System.out.println("Accessing parent class variable:"+super.a);
        System.out.println("inside B constructor");
    }

    //static block is executed first, if it is present, even before the constructor
    //sop statements are allowed inside the static block
    static{
        System.out.println("Static block executed");
    }

    // this method should not be of weaker type privelege . if the parent is public
    // this should be public. if the parent is protected it can be protected,public.
    // if parent is default, it can be default,protected,public
    public void func() {
        System.out.println("In child");
    }

}