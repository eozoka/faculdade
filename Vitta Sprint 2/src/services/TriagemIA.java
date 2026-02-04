package entities;

public class TriagemIA {

    public String analisarSintoma(String descricao) {
        if (descricao == null || descricao.trim().isEmpty()) {
            return "Indeterminada";
        }

        String analise = descricao.toLowerCase().trim();

        if (analise.contains("dor forte") || analise.contains("sangramento") || analise.contains("hemorragia")) {
            return "Alta prioridade";
        } else if (analise.contains("desconforto") || analise.contains("inchaço") || analise.contains("dor")) {
            return "Média prioridade";
        } else {
            return "Baixa prioridade";
        }
    }
}