from PIL import Image, ImageDraw, ImageFont
# Peço desculpas pelo equívoco.
# O erro ocorre porque o objeto ImageDraw não possui um atributo textsize.
# Em vez disso, você pode usar o método ImageDraw.textsize() diretamente.
# Aqui está o código corrigido:
def create_pool_ball_image(number, size=100, background_color=(255, 255, 255), ball_color=(0, 0, 255)):
    # Cria uma nova imagem com fundo transparente
    image = Image.new("RGBA", (size, size), (0, 0, 0, 0))

    # Obtém o objeto de desenho
    draw = ImageDraw.Draw(image)

    # Desenha a bola de bilhar
    draw.ellipse([(0, 0), (size, size)], fill=ball_color)

    # Carrega a fonte (substitua pelo caminho da sua fonte)
    font = ImageFont.truetype("arial.ttf", size//3)

    # Obtém o tamanho do texto
    k, l, text_width, text_height = draw.textbbox((0, 0), str(number), font)


    # Calcula a posição do número para centralizá-lo na bola
    x = (size - text_width) // 2
    y = (size - text_height) // 2

    # Desenha o número na bola de bilhar
    draw.text((x, y), str(number), font=font, fill=background_color)

    return image

def save_pool_balls():
    for number in range(1, 61):
        if number in range(1,11):
            image = create_pool_ball_image(number)
        if number in range(11, 21):
            image = create_pool_ball_image(number, ball_color=(0, 255, 0))
        if number in range(21,31):
            image = create_pool_ball_image(number, ball_color=(255, 0, 0))
        if number in range(31,41):
            image = create_pool_ball_image(number, ball_color=(64, 127, 64))
        if number in range(41,51):
            image = create_pool_ball_image(number, ball_color=(255, 0, 255))
        if number in range(51, 61):
            image = create_pool_ball_image(number, ball_color=(127, 127, 127))

        image.save(f"Fotos/{number}.png", "PNG")

if __name__ == "__main__":
    save_pool_balls()
