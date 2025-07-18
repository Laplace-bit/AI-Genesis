from sqlalchemy.orm import Session
import crud, schemas, models
from database import SessionLocal, engine
from models import Base
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
            description="OpenAI发布了其最新的旗舰模型GPT-4o，它能够实时处理和响应音频、视觉和文本的组合输入，标志着人机交互进入了一个更加自然和无缝的新纪元。这个模型在语音识别、图像理解和文本生成方面都有显著提升，为AI助手的发展开辟了新的可能性。",
            image_url="https://images.unsplash.com/photo-1677442136019-21780ecad995?w=500",
            source_url="https://openai.com/index/hello-gpt-4o/",
            tags="#大语言模型,#多模态,#里程碑,#OpenAI"
        ),
        schemas.TimelineEventCreate(
            title="Midjourney V6 发布",
            date=date(2023, 12, 21),
            description="Midjourney发布了其V6模型，显著提升了图像的真实感、细节处理能力和对提示词的理解能力，尤其在渲染文字方面取得了重大突破。新版本能够更好地理解复杂的提示词，生成更加精确和美观的图像。",
            image_url="https://images.unsplash.com/photo-1547036967-23d11aacaee0?w=500",
            source_url="https://docs.midjourney.com/docs/models-1",
            tags="#图像生成,#Midjourney,#里程碑"
        ),
        schemas.TimelineEventCreate(
            title="ChatGPT发布：AI对话的革命性突破",
            date=date(2022, 11, 30),
            description="OpenAI发布ChatGPT，这是一个基于GPT-3.5的对话式AI模型，能够进行自然、连贯的对话。ChatGPT的发布标志着AI技术从实验室走向大众，引发了全球对AI应用的广泛关注和讨论。",
            image_url="https://images.unsplash.com/photo-1676299081847-824916de030a?w=500",
            source_url="https://openai.com/blog/chatgpt",
            tags="#大语言模型,#对话AI,#里程碑,#OpenAI"
        ),
        schemas.TimelineEventCreate(
            title="Stable Diffusion开源发布",
            date=date(2022, 8, 22),
            description="Stability AI发布了Stable Diffusion，这是第一个真正开源的高质量文本到图像生成模型。它的开源特性让全世界的开发者都能够使用和改进这项技术，极大地推动了AI图像生成领域的发展。",
            image_url="https://images.unsplash.com/photo-1633356122544-f134324a6cee?w=500",
            source_url="https://stability.ai/blog/stable-diffusion-announcement",
            tags="#图像生成,#开源,#Stable Diffusion,#里程碑"
        ),
        schemas.TimelineEventCreate(
            title="DALL-E 2震撼发布",
            date=date(2022, 4, 6),
            description="OpenAI发布DALL-E 2，这个AI系统能够根据自然语言描述创建逼真的图像和艺术作品。DALL-E 2展示了AI在创意领域的巨大潜力，能够理解复杂的概念并将其转化为视觉作品。",
            image_url="https://images.unsplash.com/photo-1686191128892-4e4e0e0e0e0e?w=500",
            source_url="https://openai.com/dall-e-2",
            tags="#图像生成,#创意AI,#DALL-E,#OpenAI"
        ),
        schemas.TimelineEventCreate(
            title="GitHub Copilot正式发布",
            date=date(2021, 6, 29),
            description="GitHub与OpenAI合作推出GitHub Copilot，这是一个AI编程助手，能够根据注释和代码上下文自动生成代码。Copilot标志着AI开始深入到软件开发的核心流程中，改变了程序员的工作方式。",
            image_url="https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=500",
            source_url="https://github.blog/2021-06-29-introducing-github-copilot-ai-pair-programmer/",
            tags="#编程助手,#GitHub,#OpenAI,#开发工具"
        )
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
                difficulty="入门",
                cover_image_url="https://images.unsplash.com/photo-1556155092-490a1ba16284"
            ),
            schemas.TutorialCreate(
                title="AI辅助论文写作",
                category="by_task",
                subcategory="文案写作",
                content="详细步骤...",
                difficulty="进阶",
                cover_image_url="https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8"
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
