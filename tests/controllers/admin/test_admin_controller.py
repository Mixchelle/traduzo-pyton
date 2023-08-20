from bson import ObjectId
from src.models.history_model import HistoryModel
from src.models.user_model import UserModel


def test_history_delete(app_test):
    # Criação de um usuário para autenticação
    user = UserModel(
        name="Admin",
        level="admin",
        token="admin_token123"
    )
    user.save()

    # Criação de um registro no histórico
    history_entry = HistoryModel({
        "original_text": "Test translation",
        "translated_text": "Tradução de teste",
        "source_language": "en",
        "target_language": "pt"
    })
    history_entry.save()

    # Obtém o ID do registro do histórico
    history_id = str(history_entry.get_id())

    # Faz a requisição DELETE para excluir o registro do histórico
    response = app_test.delete(
        f"/admin/history/{history_id}",
        headers={
            "Authorization": "admin_token123",
            "User": "Admin"
        }
    )

    # Verifica se a resposta tem status 204 (No Content)
    assert response.status_code == 204

    # Verifica se o registro foi excluído
    assert HistoryModel.find_one({"_id": ObjectId(history_id)}) is None
