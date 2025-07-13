from sqlalchemy.orm import Session
from . import crud, schemas
from .database import SessionLocal, engine
from .models import Base
from datetime import date

def seed_data():
    # Create tables
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    # Check if data already exists
    if crud.get_timeline_events(db):
        print("Data already seeded.")
        db.close()
        return

    events = [
        schemas.TimelineEventCreate(
            title="GPT-4o发布：开启多模态实时交互新时代",
            date=date(2024, 5, 13),
            description="OpenAI发布了其最新的旗舰模型GPT-4o，它能够实时处理和响应音频、视觉和文本的组合输入，标志着人机交互进入了一个更加自然和无缝的新纪元。",
            image_url="https://image.cnbcfm.com/api/v1/image/107414999-1715619332024-05-13t174513z_1833596229_rc2r18ao3x2w_rtrmadp_0_openai-conference.jpeg",
            source_url="https://openai.com/index/hello-gpt-4o/",
            tags="#大语言模型, #多模态, #里程碑, #OpenAI"
        ),
        schemas.TimelineEventCreate(
            title="Midjourney V6 发布",
            date=date(2023, 12, 21),
            description="Midjourney发布了其V6模型，显著提升了图像的真实感、细节处理能力和对提示词的理解能力，尤其在渲染文字方面取得了重大突破。",
            image_url="https://cdn.midjourney.com/docs/images/v6_release_notes_upscalers.png",
            source_url="https://docs.midjourney.com/docs/models-1",
            tags="#图像生成, #Midjourney, #里程碑"
        ),
    ]

    for event in events:
        crud.create_timeline_event(db, event)

    if not crud.get_tutorials(db):
        tutorials = [
            schemas.TutorialCreate(
                title="用AI在30分钟内生成一份竞品分析报告",
                category="by_industry",
                subcategory="市场营销",
                content="详细步骤...",
                difficulty="入门"
            ),
            schemas.TutorialCreate(
                title="AI辅助论文写作",
                category="by_task",
                subcategory="文案写作",
                content="详细步骤...",
                difficulty="进阶"
            ),
        ]
        for tutorial in tutorials:
            crud.create_tutorial(db, tutorial)

    if not crud.get_prompts(db):
        # First, create a user
        user = models.User(username="jules", email="jules@example.com", hashed_password="fakehashedpassword")
        db.add(user)
        db.commit()
        db.refresh(user)

        prompts = [
            schemas.PromptCreate(
                title="赛博朋克城市",
                prompt_text="a sprawling cyberpunk city, neon signs, flying vehicles, rainy night, cinematic lighting",
                negative_prompt_text="sunny day, trees, nature",
                model="Midjourney V6",
                preview_url="https://images.unsplash.com/photo-1519681393784-d120267933ba",
                tags="#赛博朋克, #城市",
                author_id=user.id
            ),
            schemas.PromptCreate(
                title="二次元风格的女孩",
                prompt_text="a beautiful anime girl, long flowing hair, sparkling eyes, school uniform",
                negative_prompt_text="realistic, 3d",
                model="Stable Diffusion XL",
                preview_url="https://images.unsplash.com/photo-1519681393784-d120267933ba",
                tags="#二次元, #女孩",
                author_id=user.id
            ),
        ]
        for prompt in prompts:
            crud.create_prompt(db, prompt)

    print("Data seeded successfully.")
    db.close()

if __name__ == "__main__":
    seed_data()
