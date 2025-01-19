namespace overflow;
public static class Program{
    private static int overflow(string a) {
        return overflow(a);
    }
    public static int Main(string[] args) {
        Console.WriteLine("Hello!");
        
        overflow(new string('4', 64));
        return 0;
    }
    
}
