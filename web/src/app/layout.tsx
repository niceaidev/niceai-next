import '../styles/globals.css';

import { GeistSans } from 'geist/font/sans';

import { TRPCReactProvider } from '../trpc/react';
import { type PropsWithChildren } from 'react';

export { metadata } from './metadata';

export default function RootLayout({
  children,
}: PropsWithChildren) {
  return (
    <html lang="en" className={`${GeistSans.variable}`}>
    <body>
    <TRPCReactProvider>{children}</TRPCReactProvider>
    </body>
    </html>
  );
}
