import { getMovieRatePrediction } from '../services/index.js';
import { 
    getMovieDetail, 
    searchMovies 
} from '../services/tmdb.js'

export const renderIndex = async (req, res) => {
    res.render('index');
};

export const renderDetail = async (req, res) => {
    const movie_id = req.query.movie_id;

    // TMDB API로 영화 상세 데이터 요청하는 서비스 함수
    const detail = await getMovieDetail(movie_id);

    let predicted_rating = 0;

    try {
        predicted_rating = parseFloat(await getMovieRatePrediction(detail.runtime, detail.revenue))
        if (isNaN(predicted_rating)) {
            predicted_rating = 0;
        } else {
            predicted_rating = predicted_rating.toFixed(2);
        }
    } catch(err) {
        console.error('평점 예측 중 오류 발생: ', err)
    }
    // 여기서 Detail 데이터를 DB에 저장하여 데이터셋을 구성하는데 사용할 수 있으나
    // 모델의 정확도를 개선하는 방법을 찾지 못해 기능을 구현하지 못했다.

    // 감독이나 작가를 따로 표시하기 위함.
    const dnw = detail.credits?.crew?.filter(c => ['Directing', 'Writing'].includes(c.department));

    res.render(
        'detail',
        {
            detail, 
            predicted_rating,
            directors_and_writers: dnw?.splice(0, 6) || [], // dnw는 인기도순으로 정렬되어 있음.
            actors: detail.credits?.cast?.filter(c => c.known_for_department === 'Acting') || [],
            credits: detail.credits,
        }
    );
};

export const renderSearchList = async (req, res) => {
    const query = req.query;
    const searchResult = await searchMovies(query.query, query.page)

    res.render('search_list', { query: query.query, movies: searchResult });
};
