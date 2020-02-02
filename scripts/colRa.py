# colRa.py

from pandas import DataFrame, concat

# metodo para listar colegas nas mesmas turmas de ra
def colRa(df_deferidas, df_nomeras, ra, ad):

    # df das turmas matriculadas por este RA
    df_turmas_ra = df_deferidas[df_deferidas['ra'].astype(str).str.contains(ra)]

    # df final que sera exportado como csv
    df_export = DataFrame()

    # laco para cada turma
    for i, lin in df_turmas_ra.iterrows():

        # df para ras/nomes matriculados na turma atual
        df_temp = DataFrame(columns=[lin['turma']])

        # selecao dos ras matriculados na turma atual
        df_ras = df_deferidas[df_deferidas['turma'].astype(str).str.contains(lin['turma'])]

        # laco para cada ra
        for j, ljn in df_ras.iterrows():

            # selecao dos nomes dos matriculados na turma atual
            df_nome = df_nomeras[df_nomeras['ra'].astype(str).str.contains(str(ljn['ra']))]

            if not df_nome.empty:
                # laco para trocar RA por nome
                for z, lzn in df_nome.iterrows():
                    df_temp = df_temp.append({lin['turma']: lzn['nome']}, ignore_index = True)
            else:
                # se nao encontrar o nome armazena o RA
                df_temp = df_temp.append({lin['turma']: ljn['ra']}, ignore_index = True)

        # concatena o df gerado no df que sera exportado
        df_export = concat([df_export,df_temp], axis=1, sort=False)

    # exporta df para csv no endereco ad
    df_export.to_csv(ad, index = None, header=True)
    return
