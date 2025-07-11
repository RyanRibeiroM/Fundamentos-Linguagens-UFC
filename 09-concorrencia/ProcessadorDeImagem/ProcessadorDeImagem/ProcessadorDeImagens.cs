using System.Diagnostics;

public class ProcessadorDeImagens
{
    private static readonly List<string> imagens =
    [
        "foto_001.jpg", "logo_empresa.png", "paisagem_ferias.jpg", "documento_scan.png",
        "selfie_2024.jpg", "arte_digital.tiff", "diagrama_sistema.svg", "imagem_produto.jpg"
    ];

    public static void ProcessarImagem(object nomeDaImagem)
    {
        Console.WriteLine($"-> Iniciando processamento de: {nomeDaImagem}");
        Thread.Sleep(1000);
        Console.WriteLine($"<- Finalizado processamento de: {nomeDaImagem}");
    }

    public static void Main(string[] args)
    {
        Console.WriteLine("--- CONCORRÊNCIA ---");

        Console.WriteLine("\n[1] EXECUTANDO DE FORMA SEQUENCIAL...");
        Stopwatch stopwatchSequencial = Stopwatch.StartNew();

        foreach (var imagem in imagens)
        {
            ProcessarImagem(imagem);
        }

        stopwatchSequencial.Stop();
        Console.WriteLine($"\nTempo total (Sequencial): {stopwatchSequencial.Elapsed.TotalSeconds:F2} segundos.\n");

        Console.WriteLine("[2] EXECUTANDO DE FORMA CONCORRENTE...");
        Stopwatch stopwatchConcorrente = Stopwatch.StartNew();

        List<Thread> threads = [];

        foreach (var imagem in imagens)
        {
            Thread thread = new(ProcessarImagem!);
            threads.Add(thread);
            thread.Start(imagem);
        }

        foreach (var thread in threads)
        {
            thread.Join();
        }

        stopwatchConcorrente.Stop();
        Console.WriteLine($"\nTempo total (Concorrente): {stopwatchConcorrente.Elapsed.TotalSeconds:F2} segundos.\n");

        Console.WriteLine("--- COMPARAÇÃO ---");
        Console.WriteLine($"A abordagem concorrente foi {stopwatchSequencial.Elapsed.TotalSeconds / stopwatchConcorrente.Elapsed.TotalSeconds:F2}x mais rápida.");
    }
}