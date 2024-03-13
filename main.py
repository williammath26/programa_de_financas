from utilitarios import(
    cadastrar_categoria,
    cadastrar_transacao,
    saldo_total,
)
#catergorias
cadastrar_receitas = cadastrar_categoria("RECEITAS")
cadastrar_contas = cadastrar_categoria("CONTAS")
cadastrar_viagens = cadastrar_categoria("VIAGENS")
cadastrar_lazer = cadastrar_categoria("LAZER")

#transacao
cadastrar_transacao(
    descricao = "Salario Jan/2024",
    valor = 1000,
    categoria = cadastrar_receitas
    
)

cadastrar_transacao(
    descricao = "Mesada mamãe",
    valor = 500,
    categoria = cadastrar_receitas
    
)
cadastrar_transacao(
    descricao = "Futebol Flamengo",
    valor = -100,
    categoria = cadastrar_lazer
    
)
cadastrar_transacao(
    descricao = "conta de luz",
    valor = -120,
    categoria = cadastrar_contas    
)
cadastrar_transacao(
    descricao = "Rio de Janeiro",
    valor = -500,
    categoria = cadastrar_viagens
)

total = saldo_total()

print("Saldo total: ",total)