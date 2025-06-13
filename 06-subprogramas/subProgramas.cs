using System;

public class GerenciadorDeValores
{
    public void ModificarValor(int numero)
    {
        numero = 100;
    }

    public void ModificarComRef(ref int numero)
    {
        numero = 100;
    }
}

public class Teste
{
    public static void Main(string[] args)
    {
        var gerenciador = new GerenciadorDeValores();

        int val = 10;
        Console.WriteLine($"Valor original (antes): {val}");
        gerenciador.ModificarValor(val);
        Console.WriteLine($"Valor original (depois de 'ModificarValor'): {val}");

        Console.WriteLine(new string('-', 20));

        int refVal = 10;
        Console.WriteLine($"Valor ref (antes): {refVal}");
        gerenciador.ModificarComRef(ref refVal);
        Console.WriteLine($"Valor ref (depois de 'ModificarComRef'): {refVal}");
    }
}
