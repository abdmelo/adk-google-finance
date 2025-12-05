from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.outputs import LLMResult
from typing import Any, Dict, List

class TokenUsageCallback(BaseCallbackHandler):
    """Callback para imprimir contagem de tokens no formato solicitado."""
    
    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> Any:
        # Tenta extrair usage_metadata (padrão LangChain recente)
        # O response.generations é uma lista de listas (uma para cada prompt)
        # O usage_metadata geralmente está no generation ou no llm_output
        
        # Tenta pegar do llm_output (comum em Google GenAI)
        usage = response.llm_output.get("token_usage") if response.llm_output else None
        
        if not usage:
            # Tenta iterar sobre generations se o usage estiver lá
            try:
                if response.generations and response.generations[0] and response.generations[0][0].generation_info:
                    usage = response.generations[0][0].generation_info.get("usage_metadata")
            except:
                pass
        
        if usage:
            # Mapeia chaves comuns
            in_tokens = usage.get("prompt_token_count") or usage.get("input_tokens") or 0
            out_tokens = usage.get("candidates_token_count") or usage.get("output_tokens") or 0
            total_tokens = usage.get("total_token_count") or usage.get("total_tokens") or (in_tokens + out_tokens)
            
            print(f"\n[LOG] Token Usage -> Input: {in_tokens} | Output: {out_tokens} | Total: {total_tokens}")
        else:
            # Fallback se não encontrar metadados estruturados
            print("\n[LOG] Token Usage -> Não disponível nesta resposta.")
