using GerenciadorDeAssinaturas;

List<Assinatura> minhasAssinaturas = new List<Assinatura>();

minhasAssinaturas.Add(new PlanoBasico());
minhasAssinaturas.Add(new PlanoPremium());

Console.WriteLine("\n--- Minhas Assinaturas Ativas ---");

Console.WriteLine("\n--- Minhas Assinaturas Ativas ---");
Console.WriteLine(new string('-', 35));

foreach (var assinatura in minhasAssinaturas)
{
    assinatura.ExibirDetalhe();
    Console.WriteLine();
}

