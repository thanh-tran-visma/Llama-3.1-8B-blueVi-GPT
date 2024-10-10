from fastapi import Request
from fastapi.responses import JSONResponse
from app.api import HTTPStatus

async def chat_endpoint(request: Request):
    blue_vi_gpt_model = request.app.state.model
    try:
        body = await request.json()
        message = body.get("prompt", "").strip()
        if not message:
            return JSONResponse(
                status_code=HTTPStatus.BAD_REQUEST.value,
                content={"response": "No input provided."}
            )
        grammar_correction_message = blue_vi_gpt_model.grammar_correction(message)
        bot_response = blue_vi_gpt_model.get_response(grammar_correction_message)
        
        return JSONResponse(
            status_code=HTTPStatus.OK.value,
            content={
                "response": bot_response,
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            content={"response": f"An error occurred: {str(e)}"}
        )
