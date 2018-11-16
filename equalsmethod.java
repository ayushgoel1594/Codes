class equalsmethod{
    public static void main(String[] args) {
        A a = new A(5);
        A b = new A(5);

        System.out.println(a==b);
        System.out.println(a.equals(b));

        Integer c =5;
        Integer d = 5;

        System.out.println(c==d);
        System.out.println(c.equals(d));

    }
}
class A{
    int a;
    A(int n){
        a=n;
    }
    // @Override
    // public int hashCode() {
    //     return super.hashCode();
    // }
    @Override
    public boolean equals(Object obj) {
        A o = (A)obj;
        if(o.a==this.a){
            return true;
        }
        else
        return false;
    }
    
   
}