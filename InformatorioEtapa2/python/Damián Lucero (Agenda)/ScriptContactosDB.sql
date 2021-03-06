USE [ContactosDB]
GO
/****** Object:  Table [dbo].[Agenda]    Script Date: 18/9/2020 14:24:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Agenda](
	[Usuario] [varchar](50) NOT NULL,
	[id] [int] NOT NULL,
 CONSTRAINT [PK_Agenda] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Contactos]    Script Date: 18/9/2020 14:24:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Contactos](
	[Telefono] [bigint] NOT NULL,
	[Nombre] [varchar](50) NOT NULL,
	[Email] [varchar](50) NULL,
 CONSTRAINT [PK_Contactos] PRIMARY KEY CLUSTERED 
(
	[Telefono] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
INSERT [dbo].[Agenda] ([Usuario], [id]) VALUES (N'Damián', 1)
GO
INSERT [dbo].[Contactos] ([Telefono], [Nombre], [Email]) VALUES (3624112233, N'Luclia Bravo', N'')
INSERT [dbo].[Contactos] ([Telefono], [Nombre], [Email]) VALUES (3624223344, N'Pablo Giménez', N'pg.093@gmail.com')
INSERT [dbo].[Contactos] ([Telefono], [Nombre], [Email]) VALUES (3624334455, N'Romina Alvarez', N'romiA_23@gmail.com')
INSERT [dbo].[Contactos] ([Telefono], [Nombre], [Email]) VALUES (3624445566, N'Darío López', N'dariolop32@yahoo.com')
INSERT [dbo].[Contactos] ([Telefono], [Nombre], [Email]) VALUES (3624556677, N'Inés Acosta', N'acosta.ines09@Outlook.com')
INSERT [dbo].[Contactos] ([Telefono], [Nombre], [Email]) VALUES (3624667788, N'Camila Yanes', N'CamiYanes@gmail.com')
GO
