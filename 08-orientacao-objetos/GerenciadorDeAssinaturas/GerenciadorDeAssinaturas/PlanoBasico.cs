namespace GerenciadorDeAssinaturas
{
    public class PlanoBasico : Assinatura
    {
        public int LimiteDeTelas { get; private set; }
        public PlanoBasico() : base(25.90m)
        {
            LimiteDeTelas = 1;
        }

        public override void ExibirDetalhe()
        {
            Console.WriteLine($"Plano Básico - Preço: R$ {PrecoMensal}");
            Console.WriteLine($"  - Limite de {LimiteDeTelas} tela simultânea.");
            Console.WriteLine($"  - Renova em: {DataRenovacao.ToShortDateString()}");
        }
    }
}
