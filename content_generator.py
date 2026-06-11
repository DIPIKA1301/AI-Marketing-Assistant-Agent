def generate_caption(topic):

    caption = f"""
    Create engaging social media content about:
    {topic}

    Include:
    - Attractive caption
    - Relevant hashtags
    - Audience engagement ideas
    """

    return caption


topic=input("Enter topic: ")

print(generate_caption(topic))