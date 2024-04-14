import config 
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType

logging.basicConfig(level=logging.INFO)

bot=Bot(token=config.TOKEN)
dp = Dispatcher(bot)

PRICE = types.LabeledPrice(label="Подписка на 1 месяц",amount = 500*100)

@dp.message_handler(commands=['buy'])
async def buy(message: types.Message):
    if config.PAYMENTS_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id,"Тестовый платеж")

    await bot.send_invoince(message.chat.id,
                            title="Подписка на бота",
                            description="Активация подписки на 1 месяц",
                            provider_token=config.PAYMENTS_TOKEN,
                            currency="rub",
                            photo_url='data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAJAAhQMBIgACEQEDEQH/xAAcAAABBQEBAQAAAAAAAAAAAAAFAQIDBAYHAAj/xABBEAACAQMCAgYFCQYFBQAAAAABAgMABBEFIRIxBhNBUWFxFCIygZEVQkNSobHB0eEHIzNUcpNVc4KS8TRTY4Oi/8QAGgEAAgMBAQAAAAAAAAAAAAAAAgQBAwYFAP/EADERAAIBAwIFAgQEBwAAAAAAAAECAAMEEQUhEhMxQVEygRRSkaEVQmFiIiNTcaKx4f/aAAwDAQACEQMRAD8ASTS2HLfyqs9lKnINV9Z7lPaUmpBe52eOtaK7CcWnrA/MIID3EJ5nFTreI44ZloiZLdx6w86iks4H9lhRiqjdRHqeoUH7ykYUJ44HAPYKsQXUsW0gz40xrBlPqNTTHcL4gURKsOsYFSm/eE0uY5ANxnxp+Ad1IoP645rip4C+OIuqIObM2wqmoqopbO09yw20KRLI+Qqk432qG8aCC0muLiVECISA3NjjIGKF9IrySOxUW/FDG65Msp4Q4Bzld8/pWP1LWbqe2WJbgSQ+0eI5OORHFjcVw6upEkimPeWLbINyYauNSjEkfVXFsdwHYKQcnkqjO5x99W/lW5sCqXiqqsMho24lwfGueyahdQx8ERK45nAOR2fCobvWb26CieQlUACKNgBS4vbn55aGUbETrltfpdxB4ysi8sjnUolHcRXIdL1m6s7gSQTPG2e8ke8V0bRekUV8BHcxCKbkCo9Rj4fCulbagtQ8NQYMpemD6RtDXW+dKJRUfpC43X7K8Z0+r9ldLH6RY0kPUR/WCvVH16/V+yvV7h/SDyqfiEMxn6tNMcJ7BUHobdj/AG0nokgPtmqdpk+U/iStaxNTPQ1+tTeomHJqUxT/AFhXp7luJ70V19ltq91Eo+dmvBZ/rCkZmhRpZmARFLMfAVDMFBJllNKxYKuYpQRlBcEgvsioMsx8BVW61iwXghtgZmXdlLLjPIA47c9nZk9tY3V+kM8k8knWGORsoB9Re78/GhEeopJbssWUQYUONiaz1e7asTvtNjbWvJQKxyYY17XbXUJOGVHupJMBQNsDwHln34o3o3Rix6RalD6RI8McUC4hClQW5sRnfnWX6LWS/K0RuMEBtq7Dc2cdvHHeWqqHA7Ns4Un8MUo79hHadIeoyWHoF0fWFY2sVbAxkneqGs/st6OX8RMFs1rLjAkhY7e7ka2dlL1qAH2h39u1W+BscjQjMsbE+XekXRG76O6zHa3P7yGRsRygbMM/fU2lXaW1wkEjYikUCTHNTnZh4ggNXY/2l6KL7TBIq/vEOVPdXB4+LrWL+0u2O7cVYrnG8oemAdp1u04Lm0gn2BljVyB2ZFTiNKz+jauq6VbpjiZECt58/wAasNqzk+pGa1tslSrRVx3Ez1TTbpqhw20MdWndS0C+Ubk8lNepj4d/Mj8Ir/PCHpt//h6/3f1r3pt//h6f3f1qz1LH6eT3Qj868IGP01x7kQfhR5T5R95Bv7P9v+Ug9M1D+RQf+79a96VqH8nF/fP51YFsf+7cn3oPwpfRu8znzkH4CoyngQDqFn4H0Mrelah/Kw/3zQ/pBf3cOkTmWOGMSEICJC25/wCKM+jL/wCT++az/TZFi0qJlO4uBsZC/wA09hpO/Ki2fhHaMWd9a1K6qi7/ANv+zm11JJJKwds7/ZSREAgYGCeE0kjDMmOedjS2oHpUYblxjPxrLdp3ScnMOaTFcQX9m4JHHJgD4fnXVorLWtTAea69AgC8KRqAWOeZPdt99Duj3RxTqaXToOptiWjH1i2MfAZrR6tod/qZRUuZIYM+ssRwzDuzSpfJjYXAl6DR+FxLa6xM8g5I0gOceVaDT5pinBK+XA7ay2j9D7ewiaNTe8RdZOulufXUjuI3x3jlWi4xFMDR8UEqDBmrabZX7Stq11IsZHCFEpQDy8a5d036EwabDJqul3Cy2akdbvkrk8/jXU+kfRm11wxSTCbiQeqIrhoseIx21RvOicR0jUbeIOnpVqYjEzArxBcKcdhzj31OZ7AnKeiVq073Q4n6v1SpjXi338DitMtgB/M/7MfhVfoXpl3DocLG3AaUs+WTfGds0e9Buz9Go/0frWtsGNO2VSZm7u9uhWK0qewg8W+B9P8AZXqJegXfenwFepvnDzFvir/+nK/U3B2M8h8kH505bOdvnzn7PwrRIq9lOI7hSxrHxDXSLceZnhpkrcxIfN6eujsfmfFz+dGJHcctqrSSS95qRUYywabar+WVBoyjmsQ88ms1+0TShH0eWaMp+6uEL8I+acj7yK1DyP2mhnSG1a+0S9t0OZGiJTzG4+6q7lGeiwzGKFtQp1AyrgznHRjojP0gSeT0hLWINwqzKWLNz28BkVDrXR99GYsbiK4SORVd4/mk7jPdtj41rf2aXcT6dc2Ll0MModyvPgccx5EH7KNpp1jqMeq6TLN17PngmB9oAABx4g1lSW3M7oprwjHeaXo46mwtWU5BjBBzWkt5VNZLozby2Wj21vcH14l4fcDtWgiBXG9LId5ew2hhpVC1mdR1eS3l6uOzaaXi3LEqqDvzg5olqN/b6Xp7Xt7KI7dPac8hVK3v9R1MRyafp0QtmP8AHun4QRnB251cd5Wu0tWepzzTW8a2knDIuXk+ahxyoukyuCCMEc6B399qWi2r3d9b2hsYFLTGCQlowO3GPL40StLiG9t0u4M8MiZGQRke+pGZDAdZnryKCG5mQz8KhzhQeQ54qq0tkvOVm8iaqasS+qXTDPD1hAPlt+FMieFRyAbvIrXUaf8AKUnxOI75cgS2bi0+bDIw78V6hdylzK+Y51A/qxXqvFFcdYXvLaajJnZkbycVMuoyDmufLehJt7Y9gpPQofmOR5GpNMGZddYrjriGxqX1onx/Sad8pQHZhjzoF6JIPYuHH+o17q7xfZnJHjvQ8oS8a2/dRD3pdo1LxWjcz7qz3HerzEbeac6T0mUH17VPNRihNKXLrQ7r95iLi7l6GdL5pbVRNCGIMTHhEkTYYDPeO/vFaGb9oOgmCD0bT7qS5ALhGfhCN4nG/b31Fq9haXeoHVLtSsNtaOHjZieJvmfa32VzO2YKSznB5VmLm3CVSDNLbXnNpB07zt3Rfpdba5E6lOouYzh4WbPvB7RWvgnDR4r50tpGjkWW2kaGVeTocGtno3T65suGPVYTIg+miG/vH5Uo1AjdY4lyGGGnZbeZJonglCsjAghhkUMuejds8ocWsM+BsJEDAeQOwoLpPS/TL4hrS5Rz2r2jzFaW31yDhGXFAPBloON1jLHQYY5eP0G3t+/q0UEju2FENYuvQbKSVVDMq+qpIHE3ID44qH5dt8gcXltWSPTG317pD8mWkLSWsSszXGRhnH4c/fV1JA7hfMCo7Yye0vrdxSKDKuWO5LbmnZtH5oKV7RCPVqs9qy8s1qkVQMAzjkknMmNvZNvgV6qhDLtk16rOE+YPtBSfJsv8K+T3uKkFmGH7q6RvI5qi0ML+3pgJ8BGfuNMays/n2NxH4ojj7s01wr2M5R0qzf0kj3BhH0O6X2XRh54pDFdof4RPkaG9Vap7Fzewf6nH3inLOU2j1xx4SFW++p4D5+0rbQ0Ppf6iXjJMvtxSD3V43Q5OpHmKgjudQ+j1C1l8Gi/I1O8+qRQmWeGyaIcyOLPwwTQOQnqIi7aHUHpcf6lLXJYptEvouLhEkYDEd3ED+Fcqu9KaOygulO8hZWQ81IJH212jo/c2WuJfB4oSbaPiKICeMYbOdthgGsD0phka+lkCwpHcETxRxEFVUjYbfH31n9QZXrZUzt6Zb1Leiab+czFW8jwyYbPlRqJ+OMd1CrpTxcWNxzqxYS49VjSQ2jxMtG0RpFkifqpByYGiEHSDXtPXhylzGORxvUQiVtwaTDJyJrzUlaeWqy9Ju+jmrz3OmSX92kadUrP6pzyHb3UF/Z90iZo2s5oo4mVcrOvq8fg3jWWnup40ZY3K8QwcHGR3HvoloN+np9nFHboJJJVVgBgHJo7UcmqCJNzXZ6R4euJ1GLU3GwdH8nH6VaTU8j1o2x34oK0BO7WTfCmdQoP/AE0o/pBrSmmpmTXV7hfUJoPT7Y+0MHx2r1Z/hxyFyPe1LUcoSz8af5JaLynmz++MGmhsdkWf8qr3UqedqvuzS9RAFLyqI0Xm3GahqiKMtOsbOn3QSkJCBjhHwYVIFYpxzKFT/Mbf3Gqk2s6fFI4tIjMF26xmzk+AoZf21/rEbS6jcmytzIEiQOFLgczv2dgA7jzpKrejpTEEWlHxj3Mfq+qWkTdXFJbRD6xZS/xxU1nPcarYqLVyllEQss75XjPcp7fu8+VYWDR5bnXJbKAP1KzlTNjGF7/PFafpP0gj0+0j0fTUCiNQCe79a55qM+7RnhC4Amfkvni1/rbSEGWKQoygF+tTluO0jntz7sbEnfWuoaq4uEi47dUZmlKhEzjLAYwDwgDl2DNZB3Jk4z7Xb40T0rpFqlppt1oiXC/J879aUZSzDOMhT2A9tLt1zGV6YlHUrbhkO2M7e+hKkxyCtFcL1kRyckbg0GuosesBUkSBCVnLxKAasSeyaFWEmDjNEmPqGiEEiULnnS6UeHVLQnkJl7SO3vFR3By1JbHgmRvqsDXgcMDCE6uLGYHZZx/Tcv8AiKX0e5HI3o8p/wA6tqjsgYIcEZyFOPvr3Aw+aw/3VqeYTEC1fyPoZU4bsfS3/wDcSvVa9b6z/wD1XqniMjiq/t+hiN0isIouLriDtxM2eFfecUA6Q9IbW9t+ptLxI45CBLI2T6vaFx2nv2rnkt7PfMfSJWc7/bVMl42Iyay71mc5Me5eTNm/SGKzjd7dRxL6tvvleL6xxtt95HdWU1G5mu5mnuZGmmbm7nJ/4pInWUYxhu7sNenG3LFVlswlUCFNB125tIJUjCs5x6zcwN6juJHmkaWQ5dzljQ3Tv4kgq/JUgkjeQQAZDnPF4GnxKrSxM/sqw4gO1e2oUOTKBzzSysUUKCcnbaohTpFj0d6Ot0Zju7rXokvpbdyLZ50BRvm7Ddl8fKsFNFsR2HcURubO9t7Vb+VIzaxzdSXSUFSxxjgXPLsx2bVDJA72/WqjGINhXxsfDNQpyJLDBgiFTHMNqvzycEeO3FNKqrcTjAXnVG4m619uQooOI0niOacnOmCnLUQp2PozrXX6HZs4ZnWPgY55ldvwop8pp9Vq5Z0Y16axZ7PMbLIOKMTAlQ/dz2z99H06VArl7eIdhBRhg93Ou/ZGncKFHqlfLqM38M2nylF9Vvsr1Y8dKIDzgj/3MKSuh8E3yyfh7jxOW7oQRzq0hWYYYb0x1HDTIPVfFY7pLDvHyQlDlTnHKpSethzyYc6Xi7KTICnFFBjNP/iv51cfc5qlp5y7HxqxM+FavDpPHrGWv8R/E1ZOFZJSuShyB2Zxz+6qsB4F4u01aRg8fvwa9jaQTgwtBGL3ToLWVFnt5oWmmvJJCiwTDiJAPLIHDnO5z3YqiekU93YtbjMasVaVARgsF4eIbbDc7dmTVzRdPkuLCVYrV5oJQ3XtHccDIQwGAvbtg4I/TL3URsryWNZEkEbsgdN1cA4yPA0EsliWR3JySaYtX9MtFv8AHG3UKyOY5GU8LFQTw57PPy76pleFiDgkHGxzRZg4i16kzVi2tJ7rrDbxPJ1KGSThHsqOZqZ6JcxdS1vh1frIg5x2ZzsfEYq/bajLC6TRtiVcBidw3cSO3uPuoXMMdXU0fPFErEHIO8E9Z03RZ9M1WzE56tJB6skbKmVb4V6uZMzox6t2XPPBr1dBdRqgYMQezdmJFRhP/9k=',
                            photo_width=416,
                            photo_height=234,
                            photo_size=416,
                            is_flexible=False,
                            prices = [PRICE],
                            start_parametr="one-month-subscription",
                            payload="test-invoice-payload")

@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)

@dp.message_handler(content_types=ContentType.sUCCEsSFUL_PAYMENT)
async def succesfull_payment(message: types.Message):
    print("Оплачено успешно!")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        print(f"{k} = {v}")

    await bot.send_message(message.chat.id,
                           f"Платеж на сумму{message.successful_payment.total_amount // 100}")
@dp.message_handler()
async def start(message: types.Message):
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates= False)            