import os
import sys
from dotenv import load_dotenv
import typer
from rayforge.cli import app as rayforge_cli
from rayforge.deployment.gui_streamlit import st
from rayforge.deployment.serve_fastapi import serve_model
from rayforge.core.forge_engine import Forge
load_dotenv()
MODE = os.getenv("RAYFORGE_MODE", "cli").lower()
MODEL_ID = os.getenv("RAYFORGE_MODEL_ID")
MODEL_SOURCE = os.getenv("RAYFORGE_MODEL_SOURCE", "huggingface")
PORT = int(os.getenv("RAYFORGE_PORT", 7860))
def main():
    if len(sys.argv) > 1:
        rayforge_cli()

    elif MODE == "gui":
        print("🧠 Launching RayForge in Streamlit GUI mode...")
        st.run("rayforge/deployment/gui_streamlit.py")

    elif MODE == "serve":
        if not MODEL_ID:
            print("❌ You must set RAYFORGE_MODEL_ID in .env for serve mode.")
            return

        print(f"🌐 Serving model `{MODEL_ID}` from `{MODEL_SOURCE}` on port {PORT}")
        forge = Forge()
        model = forge.pull(MODEL_ID, MODEL_SOURCE)
        serve_model(model, PORT)

    elif MODE == "cli":
        print("🔧 RayForge CLI (no arguments provided). Try `--help`.")
        rayforge_cli()

    else:
        print(f"❌ Invalid mode `{MODE}`. Choose from: cli, gui, serve")


if __name__ == "__main__":
    main()
