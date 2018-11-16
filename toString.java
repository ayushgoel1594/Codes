class toString {
    public static void main(String[] args) {
        // System.out.println("ayush is great");
        A b = new B();
        System.out.println(b);
    }
}

class A {
    int a;

    A() {
        System.out.println("A");
    }

    A(int c) {
        System.out.println(c);
    }

    // if this is commented hashcode of the object will be printed on printing the
    // object
    public String toString(){
    return "Ayush64648";
    }

}

class B extends A {
    int b;

    B() {
        super(5);
        System.out.println("B");
    }
}