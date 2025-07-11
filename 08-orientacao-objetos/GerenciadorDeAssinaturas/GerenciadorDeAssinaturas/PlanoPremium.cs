namespace GerenciadorDeAssinaturas
{
    public class PlanoPremium : Assinatura
    {
        public int LimiteDeTelas { get; private set; }
        public bool Qualidade4k { get; private set; }
        public PlanoPremium() : base(55.90m)
        {
            LimiteDeTelas = 4;
            Qualidade4k = true;
        }

        public override void ExibirDetalhe()
        {
            string qualidade = Qualidade4k ? "Sim" : "Não";
            Console.WriteLine($"Plano Premium - Preço: R$ {PrecoMensal}");
            Console.WriteLine($"  - Limite de {LimiteDeTelas} tela simultânea.");
            Console.WriteLine($"  - Qualidade 4k Ultra HD: {qualidade}");
            Console.WriteLine($"  - Renova em: {DataRenovacao.ToShortDateString()}");
        }
    }
}
