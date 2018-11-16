class String_Concept{
    public static void main(String[] args) {
        String a= new String("ayush");
        StringBuffer db= new StringBuffer("goel ");
        db.append(a);
        System.out.println(db.reverse());
    }
}