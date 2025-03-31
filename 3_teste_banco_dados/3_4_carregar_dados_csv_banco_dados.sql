-- Carregando os dados CSV no banco de dados, tanto do Relatório
-- quanto das Demonstrações Contábeis

COPY operadoras_saude(
  registro_ans, cnpj, razao_social, nome_fantasia, modalidade,
  logradouro, numero, complemento, bairro, cidade, uf, cep,
  ddd, telefone, fax, endereco_eletronico, representante,
  cargo_representante, data_registro
) FROM './dados_cadastrais/Relatorio_cadop.csv'
DELIMITER ";"
CSV HEADER;

COPY demonstracoes_contabeis(
  competencia, registro_ans, cnpj, receita, despesa, resultado,
  patrimonio_liquido
) FROM './demonstracoes_contabeis_extraidos/1T2023.csv'
DELIMITER ";"
CSV HEADER;