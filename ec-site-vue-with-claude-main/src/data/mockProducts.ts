import { fetchProducts } from "./products";

export interface Review {
  id: number;
  userName: string;
  rating: number;
  comment: string;
}

export interface Product {
  id: number;
  name: string;
  price: number;
  salePrice?: number;
  image: string;
  description: string;
  categoryId: number;
  reviews: Review[];
}

const generateReviews = (): Review[] => {
  const reviewCount = Math.floor(Math.random() * 3) + 1; // 1-3 reviews per product
  const reviews: Review[] = [];
  for (let i = 0; i < reviewCount; i++) {
    reviews.push({
      id: i + 1,
      userName: `ユーザー${Math.floor(Math.random() * 1000)}`,
      rating: Math.floor(Math.random() * 5) + 1,
      comment: `この商品は${['とても良い', '素晴らしい', '使いやすい', 'デザインが素敵な'][Math.floor(Math.random() * 4)]}です。`
    });
  }
  return reviews;
};

const generateProducts = (categoryId: number, startId: number): Product[] => {
  const products: Product[] = [];
  const categories = ['キッチン', 'インテリア', 'ステーショナリー', 'ガーデニング'];
  const categoryName = categories[categoryId - 1];

  for (let i = 0; i < 10; i++) {
    const id = startId + i;
    const isSale = i < 3; // 最初の3つの商品をセール対象にする
    const price = Math.floor(Math.random() * 5000) + 1000;
    const salePrice = isSale ? Math.floor(price * 0.8) : undefined;

    products.push({
      id,
      name: `${categoryName}アイテム${i + 1}`,
      price,
      salePrice,
      image: `/images/products/${categoryName.toLowerCase()}${i + 1}.jpg`,
      description: `${categoryName}カテゴリーの素敵なアイテムです。使いやすさとデザイン性を兼ね備えています。`,
      categoryId,
      reviews: generateReviews()
    });
  }

  return products;
};

export const mockProducts: Product[] = [
  ...(await fetchProducts()),   // キッチン
  ...generateProducts(2, 11),  // インテリア
  ...generateProducts(3, 21),  // ステーショナリー
  ...generateProducts(4, 31),  // ガーデニング
];

export const getProductById = (id: number): Product | undefined => {
  return mockProducts.find(product => product.id === id);
};

export const getProductsByCategory = (categoryId: number): Product[] => {
  return mockProducts.filter(product => product.categoryId === categoryId);
};

export const getRecommendedProducts = (): Product[] => {
  return mockProducts.sort(() => 0.5 - Math.random()).slice(0, 4);
};

export const getSaleProducts = (): Product[] => {
  return mockProducts.filter(product => product.salePrice !== undefined).sort(() => 0.5 - Math.random()).slice(0, 4);
};