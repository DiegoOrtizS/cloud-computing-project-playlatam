import { GetServerSideProps, GetServerSidePropsContext } from "next";
import JSX from "next";
import PokemonDTO from "context/dto/PokemonDTO";
import "bootstrap/dist/css/bootstrap.min.css";
import Detail from "components/detail/Detail";
import { getPokemonDetail } from "../../../use_cases/pokemon/getPokemonDetail";

export const getServerSideProps: GetServerSideProps<PokemonDTO> = async (
  ctx: GetServerSidePropsContext
) => {
  try {
    const { tournament_id, pokemon_name } = ctx.query as { tournament_id: string, pokemon_name: string };
    const response = await getPokemonDetail(tournament_id, pokemon_name);
        
    return {
      props: response.data,
    };
  } catch {
    return {
      notFound: true,
    };
  }
};


const DetailPage = (props: PokemonDTO) => {
  return <Detail {...props} />;
}

export default DetailPage;