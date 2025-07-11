using System.Data;

namespace GerenciadorDeAssinaturas
{
    public abstract class Assinatura
    {
        public decimal PrecoMensal { get; protected set; }
        public DateTime DataRenovacao { get; protected set; }

        public Assinatura(decimal precoMensal)
        {
            PrecoMensal = precoMensal;
            DataRenovacao = DateTime.Now.AddMonths(1);
        }

        public abstract void ExibirDetalhe();

    }
}
