from api.charLimits import getAttrsLimits, getHpLimits

def buildMessage(objectName, charLevel):

    attributes = "Força, Destreza, Inteligência, Carisma, Percepção, Pontos de vida, Classe(Guerreiro/Mago/Ladrão/Paladino/Arqueiro)"

    model = f"NAME:(nome inventado para o personagem)/ALG: (personalidade)/CLASS:(classe)/RACE:(raça)/PRO: (proficiência)/HP:(pontos de vida)/STR:(valor de força)/DEX:(valor de destreza)/CAR:(valor de carisma)/PER:(valor de percepção)/WIS:(valor de inteligência)/WEA: (arma medieval)/BKG:(história do personagem)"\

    message = f"Crie uma ficha de personagem de RPG baseado num(a) {objectName}."\
        f"Crie um nome relacionado e valores de {getAttrsLimits(charLevel)} dos atributos (os pontos de vida vão de {getHpLimits(charLevel)}): {attributes}."\
        f"Depois, crie uma história para tal e coloque em APENAS UM parágrafo." \
        f"Selecione uma das classes: Guerreiro/Mago/Ladrão/Paladino/Clérigo/Druída/Bárbaro/Monge/Samurai/Artífice" \
        f"Selecione uma das raças: Halfling/Elfo/Anão/Tiefling/Humano/Draconato/Gnomo/Meio-orc/Meio-elfo" \
        f"Escolha uma personalidade: Ordeiro e bom/Ordeiro e neutro/Ordeiro e mau/Neutro e bom/Neutro/Neutro e mau/Caótico e bom/Caótico e neutro/Caótico e mau" \
        f"Defina uma proficiência: Perícia/Ferramentas/Armas/Armaduras/Testes/Magia" \
        f"Por fim, escolha apenas uma arma medieval de corpo a corpo existente para equipamento inicial" \
        f"O resultado deve seguir o seguinte modelo: {model}"
    
    return message