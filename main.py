import enum


class Status(enum.Enum):
    """
    Enum para representar os status possíveis de uma tarefa.
    """

    PENDENTE = 0
    EM_PROGRESSO = 1
    COMPLETA = 2


class Tarefa:
    """
    Classe para representar uma tarefa.
    """

    def __init__(
        self,
        tarefaId: int,
        descricao: str,
        data_de_criacao: str,
        status: Status,
        prazo: str,
        urgencia: bool,
    ) -> None:
        self.tarefaId = tarefaId
        self.descricao = descricao
        self.data_de_criacao = data_de_criacao
        self.status = status
        self.prazo = prazo
        self.urgencia = urgencia


class ListaTarefas:
    """
    Classe para representar uma lista de tarefas.
    """

    tarefas: list[Tarefa] = []

    def __init__(self) -> None:
        self.tarefas = []

    def adicionar_tarefa(self, tarefa: Tarefa) -> None:
        """
        Permitir ao usuário adicionar uma nova tarefa à lista de tarefas pendentes.
        """
        self.tarefas.append(tarefa)

    def listar_tarefas(self) -> None:
        """
        Mostrar todas as tarefas pendentes na lista, enumerando-as.
        """
        for tarefa in self.tarefas:
            if tarefa.status == Status.PENDENTE:
                print(
                    f"""
ID da tarefa: {tarefa.tarefaId}
Descrição: {tarefa.descricao}
Data de criação: {tarefa.data_de_criacao}
Status: {tarefa.status.name}
Prazo: {tarefa.prazo}
Urgência: {tarefa.urgencia}
"""
                )

    def marcar_tarefa_como_concluida(self, tarefaId: int) -> None:
        """
        Permitir ao usuário marcar uma tarefa como concluída.
        """
        for tarefa in self.tarefas:
            if tarefa.tarefaId == tarefaId:
                tarefa.status = Status.COMPLETA
                break
        else:
            print("Tarefa não encontrada.")

    def remover_tarefa(self, tarefaId: int) -> None:
        """
        Permitir ao usuário remover uma tarefa da lista.
        """
        for tarefa in self.tarefas:
            if tarefa.tarefaId == tarefaId:
                self.tarefas.remove(tarefa)
                break
        else:
            print("Tarefa não encontrada.")


def main():
    tarefa1 = Tarefa(1, "Tarefa 1", "2026-01-01", Status.PENDENTE, "2026-01-01", True)
    tarefa2 = Tarefa(2, "Tarefa 2", "2026-01-02", Status.PENDENTE, "2026-01-02", False)
    tarefa3 = Tarefa(3, "Tarefa 3", "2026-01-03", Status.PENDENTE, "2026-01-03", True)
    tarefa4 = Tarefa(4, "Tarefa 4", "2026-01-04", Status.PENDENTE, "2026-01-04", False)
    tarefa5 = Tarefa(5, "Tarefa 5", "2026-01-05", Status.PENDENTE, "2026-01-05", True)
    lista_tarefas = ListaTarefas()
    lista_tarefas.adicionar_tarefa(tarefa1)
    lista_tarefas.adicionar_tarefa(tarefa2)
    lista_tarefas.adicionar_tarefa(tarefa3)
    lista_tarefas.adicionar_tarefa(tarefa4)
    lista_tarefas.adicionar_tarefa(tarefa5)

    lista_tarefas.listar_tarefas()
    lista_tarefas.marcar_tarefa_como_concluida(1)
    lista_tarefas.listar_tarefas()
    lista_tarefas.remover_tarefa(2)
    lista_tarefas.listar_tarefas()


if __name__ == "__main__":
    main()
